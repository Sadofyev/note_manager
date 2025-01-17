username = input("Пользователь: ")
title = input("Заголовок: ")
content = input("Описание: ")
status = input("Cтатус: ")
created_date = input("Создано (дд.мм.гггг): ")
issue_date = input("Исполнить до (дд.мм.гггг): ")


print("Пользователь: "+username)
print("Заголовок: "+title)
print("Описание: "+content)
print("Cтатус: "+status)
print("Создано: "+created_date[0:5])
print("Исполнить до: "+issue_date[0:5])