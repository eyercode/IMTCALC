from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        kg = float(weight_tf.get())
        m = float(height_tf.get()) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)
    
        if bmi < 18.5:
            messagebox.showinfo('Результат ИМТ', f'ИМТ = {bmi}\nНедостаточный вес')
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo('Результат ИМТ', f'ИМТ = {bmi}\nНормальный вес')
        elif 25 <= bmi < 29.9:
            messagebox.showinfo('Результат ИМТ', f'ИМТ = {bmi}\nИзбыточный вес')
        else:
            messagebox.showinfo('Результат ИМТ', f'ИМТ = {bmi}\nОжирение')  
    except ValueError:
        messagebox.showerror('Ошибка ввода', 'Пожалуйста, введите корректные данные')

# Создаем основное окно
window = Tk()
window.title('Калькулятор ИМТ')
window.geometry('400x400')
window.config(bg='#f5f5f5')  # Светлый нейтральный фон

# Создаем фрейм для контейнера элементов с тенью
frame = Frame(window, padx=30, pady=30, bg='#f5f5f5', bd=2, relief="solid", borderwidth=2)
frame.pack(expand=True)

# Шрифты для элементов
font_label = ('Helvetica', 14)
font_button = ('Helvetica', 16, 'bold')

# Заголовок с тенью
title_label = Label(frame, text="Введите данные для расчета", font=('Helvetica', 18, 'bold'), bg='#f5f5f5', fg='#333', pady=10)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Метки для ввода
height_lb = Label(frame, text="Рост (см):", font=font_label, bg='#f5f5f5', fg='#333')
height_lb.grid(row=1, column=0, sticky='w', padx=10)

weight_lb = Label(frame, text="Вес (кг):", font=font_label, bg='#f5f5f5', fg='#333')
weight_lb.grid(row=2, column=0, sticky='w', padx=10)

# Поля ввода с округленными углами и тенями
height_tf = Entry(frame, font=font_label, width=20, borderwidth=2, relief="solid", bg='#e0e0e0', fg='#333', justify="center", bd=0)
height_tf.grid(row=1, column=1, pady=10)
height_tf.config(highlightbackground="#ccc", highlightthickness=1)  # Добавляем тонкую рамку

weight_tf = Entry(frame, font=font_label, width=20, borderwidth=2, relief="solid", bg='#e0e0e0', fg='#333', justify="center", bd=0)
weight_tf.grid(row=2, column=1, pady=10)
weight_tf.config(highlightbackground="#ccc", highlightthickness=1)

# Кнопка с мягкими углами и тенью
cal_btn = Button(frame, text='Рассчитать ИМТ', command=calculate_bmi, font=font_button, bg='#6200ea', fg='white', relief="flat", width=20, height=2)
cal_btn.grid(row=3, column=0, columnspan=2, pady=20)
cal_btn.config(borderwidth=0, highlightbackground="#6200ea", highlightthickness=0)

# Добавление тени на фрейм
frame.config(bd=5, relief="solid", bg="#ffffff", highlightbackground="#6200ea", highlightthickness=2)

# Запуск главного цикла
window.mainloop()