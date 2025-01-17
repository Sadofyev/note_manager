username = input("Пользователь: ")
title0 = input("Заголовок: ")
title1 = input("Тип литературы: ")
title2 = input("Новая или перечитывание: ")
title3 = input("Вид книги: ")
title = [title0, title1, title2, title3]
content = input("Описание: ")
status = input("Cтатус: ")
created_date = input("Создано (дд.мм.гггг): ")
issue_date = input("Исполнить до (дд.мм.гггг): ")

note = [
    username,
    [title0, title1, title2, title3],
    content,
    status,
    created_date,
    issue_date
]

print("Пользователь: "+username)
print("Заголовок: "+title[0])
print("Тип литературы: "+title[1])
print("Новая или перечитывание: "+title[2])
print("Вид книги: "+title[3])
print("Описание: "+content)
print("Cтатус: "+status)
print("Создано: "+created_date[0:5])
print("Исполнить до: "+issue_date[0:5])