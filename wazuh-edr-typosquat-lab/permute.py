import itertools
import string

def domain_variants(domain_name, suffix):
    """
    domain_name: the core brand name, e.g. 'irctc'
    suffix: the TLD/suffix, e.g. 'co.in'
    Returns a set of candidate typosquat domains.
    """
    variants = set()
    keyboard_adjacent = {
        'a': 'qws', 'b': 'vgh', 'c': 'xdf', 'd': 'serf', 'e': 'wsdr',
        'f': 'drtg', 'g': 'ftyh', 'h': 'gyuj', 'i': 'ujko', 'j': 'huik',
        'k': 'jiol', 'l': 'kop', 'm': 'njk', 'n': 'bhjm', 'o': 'iklp',
        'p': 'ol', 'q': 'wa', 'r': 'edft', 's': 'awedxz', 't': 'rfgy',
        'u': 'yhji', 'v': 'cfgb', 'w': 'qase', 'x': 'zsdc', 'y': 'tghu',
        'z': 'asx'
    }

    # 1. Omission - drop one character at a time
    for i in range(len(domain_name)):
        variants.add(domain_name[:i] + domain_name[i+1:])

    # 2. Insertion - add each letter of the alphabet at each position
    for i in range(len(domain_name) + 1):
        for c in string.ascii_lowercase:
            variants.add(domain_name[:i] + c + domain_name[i:])

    # 3. Transposition - swap adjacent characters
    for i in range(len(domain_name) - 1):
        chars = list(domain_name)
        chars[i], chars[i+1] = chars[i+1], chars[i]
        variants.add(''.join(chars))

    # 4. Substitution - replace each char with a keyboard-adjacent key
    for i, c in enumerate(domain_name):
        for adj in keyboard_adjacent.get(c, ''):
            variants.add(domain_name[:i] + adj + domain_name[i+1:])

    # Combine each name variant with the original suffix
    full_domains = {f"{v}.{suffix}" for v in variants if v}

    # 5. TLD swaps - same core name, wider range of common/abused suffixes
    common_tlds = [
        'com', 'in', 'net', 'org', 'org.in', 'net.in', 'co',
        'xyz', 'info', 'biz', 'live', 'online', 'eu', 'de', 'app',
        'site', 'top', 'club', 'shop'
    ]
    for tld in common_tlds:
        full_domains.add(f"{domain_name}.{tld}")

    # 6. Dictionary prefixes/suffixes - common words attackers prepend/append
    dictionary_words = ['my', 'secure', 'login', 'www', 'account', 'verify', 'app']
    for word in dictionary_words:
        full_domains.add(f"{word}{domain_name}.{suffix}")
        full_domains.add(f"{domain_name}{word}.{suffix}")

    return full_domains

if __name__ == "__main__":
    target_name = "irctc"
    target_suffix = "co.in"
    results = domain_variants(target_name, target_suffix)
    print(f"Generated {len(results)} candidate domains")
    for d in sorted(results)[:20]:
        print(d)
