from tkinter import *

root = Tk()
root.title("DB_Transfer")

# 윈도우 화면 정중앙에 위치시키기 위한 작업
windows_width = root.winfo_screenwidth()
windows_height = root.winfo_screenheight()

# 생성할 App의 가로 * 세로 크기
app_width = 800
app_height = 600

# 화면 중앙에 위치시키기 위한 부분
center_width = (windows_width / 2) - (app_width / 2)
center_height = (windows_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(center_width)}+{int(center_height)}")

# DB 프레임 (DB 종류 선택, DB 필수값 입력)
db_frame = Frame(root)
db_frame.pack()

btn_db_kind = Button(db_frame, text="DB종류")
btn_db_kind.pack(side="left")


root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()
