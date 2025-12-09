import dns.resolver
import sys
import re

SPECIAL_USE_TLDS = {
    'local', 'localhost', 'intranet', 'internal', 'private', 'corp',
    'home', 'lan', 'home.arpa', 'home.arpa', 'localdomain', 'domain',
    'test', 'example', 'invalid', 'onion'
}

EMAIL_REGEX = re.compile(r"^[^@]+@([^@]+\.[^@]+)$")


def is_special_tld(domain):
    parts = domain.lower().split('.')
    for i in range(1, min(4, len(parts))):
        tld = '.'.join(parts[-i:])
        if tld in SPECIAL_USE_TLDS or tld.endswith('.local') or tld.endswith('.lan'):
            return True
    return False


def extract_domain(email):
    match = EMAIL_REGEX.search(email.strip().lower())
    return match.group(1) if match else None


def check_mx(domain):
    if is_special_tld(domain):
        return False

    try:
        records = dns.resolver.resolve(domain, "MX")
        if records:
            return True
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return None
    except Exception as ex:
        return
    return False


def check_email(email):
    domain = extract_domain(email)
    if domain:
        status = check_mx(domain)

        if status is None:
            return "домен отсутствует"
        elif status:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"
    else:
        return "домен отсутствует"

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, encoding="utf-8") as f:
            emails = [line.strip() for line in f]
    else:
        print("передайте при запуске в аргументы путь к файлу с адресами")
        sys.exit(1)

    for email in emails:
        status = check_email(email)
        print(email, status, sep="\t")


if __name__ == "__main__":
    main()