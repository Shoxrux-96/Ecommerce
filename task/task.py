import random

words = ["tiger", "tree", "underground", "giraffe", "chair"]
selected_word = random.choice(words)

def play_game(word):
    attempts = 0
    correct_guesses = []

    print("O'yin boshlandi! Kelgan so'zni toping.")
    while True:
        guess = input("Harf kiriting: ").lower()

        if guess.isalpha() and len(guess) == 1:
            attempts += 1

            # Harfning to'g'ri bo'lishini tekshirish
            if guess in word:
                correct_guesses.append(guess)
                print(f"Topdingiz! {len(correct_guesses)}-chi harf to'g'ri.")
            else:
                print("Notog'ri harf. Qayta urunib ko'ring.")

            # Barcha harflarni topish shartini tekshirish
            if set(correct_guesses) == set(word):
                print(f"Tabriklayman, siz {attempts} urinishda topdingiz. So'z: {selected_word}")
                break
        else:
            print("Noto'g'ri kirish. Iltimos, faqat harf kiriting.")

        if attempts >= len(selected_word) + 5:
            print("Urinishlar soni tugagan. Siz yutqazdingiz.")
            print(f"Urinishlaringiz tugadi. So'z: {selected_word}")
            break

play_game(selected_word)

