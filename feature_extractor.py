from urllib.parse import urlparse
import re
import ipaddress

def is_ip_address(url):
    try:
        ipaddress.ip_address(url)
        return 1
    except ValueError:
        return 0

def has_url_shortening_service(url):
    shortening_services = [
        "bit.ly", "goo.gl", "tinyurl.com", "ow.ly", "t.co", "bit.do", "shorte.st",
        "adf.ly", "is.gd", "cli.gs", "yfrog.com", "migre.me", "ff.im", "tiny.cc"
    ]
    for service in shortening_services:
        if service in url:
            return 1
    return 0

def count_subdomains(domain):
    # Remove www.
    if domain.startswith("www."):
        domain = domain[4:]
    # Count subdomains ignoring empty parts
    parts = domain.split('.')
    # Remove TLD and SLD (last two parts)
    if len(parts) > 2:
        subdomains = parts[:-2]
    else:
        subdomains = []
    return len([s for s in subdomains if s])

def extract_features(url):
    features = []

    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    # 1. Using IP address
    features.append(is_ip_address(domain))

    # 2. URL length
    features.append(len(url))

    # 3. URL shortening service
    features.append(has_url_shortening_service(url))

    # 4. '@' symbol in URL
    features.append(1 if '@' in url else 0)

    # 5. Redirecting using '//' in path (not in protocol)
    features.append(1 if '//' in parsed_url.path else 0)

    # 6. Prefix or suffix separated by '-'
    features.append(1 if '-' in domain else 0)

    # 7. Subdomain count
    subdomain_count = count_subdomains(domain)
    # Feature: 0 = no subdomain, 1 = one subdomain, 2 = multiple subdomains
    if subdomain_count == 0:
        features.append(0)
    elif subdomain_count == 1:
        features.append(1)
    else:
        features.append(2)

    # 8. HTTPS token in domain part (only if not at start)
    features.append(1 if 'https' in domain[1:] else 0)

    # 9. Presence of 'http' or 'https' in netloc (suspicious, not at start)
    features.append(1 if re.search(r'http|https', domain[1:]) else 0)

    # 10. Count of dots in domain
    features.append(domain.count('.'))

    # 11. Count of hyphens in domain
    features.append(domain.count('-'))

    # 12. Count of '@' in domain
    features.append(domain.count('@'))

    # 13. Count of digits in URL
    features.append(len(re.findall(r'\d', url)))

    # 14. Count of special characters in URL (e.g., ?, =, &, %, $, #)
    special_chars = re.findall(r'[?=&%$#]', url)
    features.append(len(special_chars))

    # 15. Length of domain
    features.append(len(domain))

    # 16. Number of subdirectories in path
    path_parts = parsed_url.path.split('/')
    features.append(len([p for p in path_parts if p]))

    # 17. Presence of port number (non-standard port)
    features.append(1 if parsed_url.port and parsed_url.port not in [80, 443] else 0)

    # 18. Presence of HTTPS in scheme
    features.append(1 if parsed_url.scheme == 'https' else 0)

    # 19. Count of query parameters
    features.append(len(parsed_url.query.split('&')) if parsed_url.query else 0)

    # 20. Length of query string
    features.append(len(parsed_url.query))

    # 21. Presence of fragment
    features.append(1 if parsed_url.fragment else 0)

    # 22. Count of hyphens in path
    features.append(parsed_url.path.count('-'))

    # 23. Count of dots in path
    features.append(parsed_url.path.count('.'))

    # 24. Count of digits in domain
    features.append(len(re.findall(r'\d', domain)))

    # 25. Count of underscores in URL
    features.append(url.count('_'))

    # 26. Count of percent encoding in URL (%)
    features.append(url.count('%'))

    # 27. Count of double slashes in path
    features.append(parsed_url.path.count('//'))

    # 28. Placeholder for domain age (WHOIS) - set to 0 for now
    features.append(0)

    # 29. Placeholder for DNS record existence - set to 1 (assume exists)
    features.append(1)

    # 30. Placeholder for Alexa rank or traffic - set to 0 (unknown)
    features.append(0)

    return features
