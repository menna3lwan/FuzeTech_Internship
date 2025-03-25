def max_vowels(s: str, k: int) -> int:
    def is_vowel(c: str) -> bool:
        return c in {'a', 'e', 'i', 'o', 'u'}


    vowel_count = sum(is_vowel(c) for c in s[:k])
    max_vowel_count = vowel_count


    for i in range(k, len(s)):
        vowel_count += is_vowel(s[i])
        vowel_count -= is_vowel(s[i - k])
        max_vowel_count = max(max_vowel_count, vowel_count)

    return max_vowel_count

