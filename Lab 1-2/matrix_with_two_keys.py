import numpy as np
import matplotlib.pyplot as plt

def generate_key_order(key):
    # Створюємо список індексів для відсортування
    indices = list(range(len(key)))
    print(f"Indices: {indices}")
    # Сортуємо індекси на основі ключа
    sorted_indices = sorted(indices, key=lambda index: key[index])
    print(f"\nSorted indices: {sorted_indices}")
    return sorted_indices

def visualize_matrix_encryption(message, row_key, col_key):
    row_order = generate_key_order(row_key)
    col_order = generate_key_order(col_key)
    
    message = message.replace(" ", "")
    matrix_size = len(row_key) * len(col_key)
    padding = matrix_size - len(message)
    message += " " * padding
    
    matrix = np.array(list(message)).reshape(len(row_key), len(col_key))
    
    fig, axes = plt.subplots(2, 3, figsize=(20, 16))
    plt.suptitle("Процес матричного шифрування", fontsize=16, y=0.98)
    
    def plot_matrix(ax, data, title, row_labels, col_labels, text_state):
        im = ax.imshow([[1 if c != ' ' else 0 for c in row] for row in data], cmap='Blues')
        title_with_text = f"{title}\n({text_state})"
        ax.set_title(title_with_text)
        
        # Додаємо межі для кожної комірки (щоб було видно окремі квадрати)
        for i in range(len(row_labels) + 1):
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(len(col_labels) + 1):
            ax.axvline(j - 0.5, color='black', linewidth=1)
        
        for i in range(len(row_labels)):
            for j in range(len(col_labels)):
                ax.text(j, i, data[i, j], ha='center', va='center', color='yellow', fontweight='bold')
        
        ax.set_xticks(range(len(col_labels)))
        ax.set_yticks(range(len(row_labels)))
        ax.set_xticklabels(col_labels)
        ax.set_yticklabels(row_labels)
    
    # Оригінальна матриця
    plot_matrix(axes[0, 0], matrix, "1. Оригінальна матриця", row_key, col_key, 
                f"Текст: {message.strip()}")
    
    # Матриця після перестановки рядків
    row_permuted = matrix[row_order]
    plot_matrix(axes[0, 1], row_permuted, "2. Після перестановки рядків", 
                [row_key[i] for i in row_order], col_key,
                f"Текст: {''.join(row_permuted.flatten()).strip()}")
    
    # Матриця після перестановки стовпців
    final_matrix = row_permuted[:, col_order]
    plot_matrix(axes[0, 2], final_matrix, "3. Після перестановки стовпців", 
                [row_key[i] for i in row_order], [col_key[i] for i in col_order],
                f"Текст: {''.join(final_matrix.flatten()).strip()}")
    
    # Процес дешифрування
    plot_matrix(axes[1, 0], final_matrix, "4. Зашифрована матриця", 
                [row_key[i] for i in row_order], [col_key[i] for i in col_order],
                f"Текст: {''.join(final_matrix.flatten()).strip()}")
    
    # Матриця після зворотної перестановки стовпців
    col_restored = final_matrix[:, np.argsort(col_order)]
    plot_matrix(axes[1, 1], col_restored, "5. Після зворотної перестановки стовпців", 
                [row_key[i] for i in row_order], col_key,
                f"Текст: {''.join(col_restored.flatten()).strip()}")
    
    # Матриця після зворотної перестановки рядків
    final_restored = col_restored[np.argsort(row_order)]
    plot_matrix(axes[1, 2], final_restored, "6. Після зворотної перестановки рядків", 
                row_key, col_key,
                f"Текст: {''.join(final_restored.flatten()).strip()}")
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    plt.subplots_adjust(hspace=0.5)  # Збільшуємо відстань між рядками підграфіків
    plt.show()
    
    print(f"Оригінальне повідомлення: {message.strip()}")
    print(f"Зашифроване повідомлення: {''.join(final_matrix.flatten()).strip()}")
    print(f"Розшифроване повідомлення: {''.join(final_restored.flatten()).strip()}")

# Приклад використання
message = "програмне забезпечення "
row_key = "шифр"
col_key = "крипто"

visualize_matrix_encryption(message, row_key, col_key)