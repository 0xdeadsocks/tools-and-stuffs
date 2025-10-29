import itertools

words = ['', '3005', '556', 'Pochita']
symbols = ['', '.', '!', '@']

# Generate all permutations of words (length 2 to len(words)) to get different orders/combinations
max_len = len(words)
with open("passlist.txt", "w") as file:
    for r in range(2, max_len + 1):  # You can start from 1 if you want single-word passwords too
        word_combos = itertools.product(words, repeat=r)
        for words_combo in word_combos:
            # Now insert symbols between words
            # For n words, you have (n-1) symbol positions
            symbol_positions = itertools.product(symbols, repeat=r - 1)
            for sym_combo in symbol_positions:
                password = ""
                for i in range(r - 1):
                    password += words_combo[i] + sym_combo[i]
                password += words_combo[-1]  # Add the last word
                if password:  # Ignore empty ones
                    file.write(password + "\n")

