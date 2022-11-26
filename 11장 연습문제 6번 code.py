import pickle                             # 리스트나 클래스 이외의 자료형은 일반적인 파일 입출력방법으로는 데이터를 저장 또는 불러올 수 없다. 텍스트 이외의 자료형을 파일로 저장하기 위해
                                          # 라이브러리에서 pickle 모듈을 불러온다 
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E , Frame # tkinter 라이브러리에서 모듈을 불러온다
phone_book = { }                          # 핸드폰 전화번호부를 딕셔너리로 지정한다
current = 0                               # current 값은 0으로 지정한다 
name = ""                            
phone = ""
window = Tk()                             # 윈도우 창을 꺼낸다 
frame1 = Frame(window)                    # Frame을 사용해 변수 frame1에 저장한다  
frame1.pack()                             # pack()을 이용하여 frame의 위치를 설정한다
Label(frame1, text = "이름 ").grid(row = 1, column = 1, sticky = W)       # Label 을 사용하여 frame1에 '이름'을 출력하고 그 크기를 정하게하는 문장이다
nameEntry = Entry(frame1, textvariable = name, width = 30)                # entry를 사용하여 이름을 입력받을 공간을 정하고 그 크기를 nameEntry라는 변수에 저장한다다
nameEntry.grid(row = 1, column = 2)                                       # nameEntry의 행과 열을 정하는 문장이다
frame2 = Frame(window)                                                    # 위와 같은방법으로 frame2를 설정한다.
frame2.pack()                                                             # pack()을 이용해 frame2의 위치를 정한다. frame2의 위치는 frame1의 아래가 될 것이다.
Label(frame2, text = "전화번호").grid(row = 1, column = 1, sticky = W)    # Label 을 사용하여 frame2에 '전화번호'을 출력하고 그 크기를 정하게하는 문장이다
phoneEntry = Entry(frame2, textvariable = phone, width = 30)               # entry를 사용하여 '전화번호' 옆에 입력할 빈 공간을 만들고 그 크기를 결정하는 문장이다    
phoneEntry.grid(row = 1, column = 2)                                       # 윗 문장에서 말한 entry의 크기를 정한다.
frame3 = Frame(window)                                                     # 세번째 프레임을 설정하고
frame3.pack()                                                              # 그 위치는 frame1과 frame2의 아랫쪽이 될 것이다
def save():                                                    # save 함수를 저장한다            
 outfile = open("phonebook.dat", "wb")                         # "phonebook.dat"을 wb방식으로 열어 변수 outline에 저장한다.
                                                               # pickle로 데이터를 저장하거나 불러올때는 파일을 바이트 형식인  wb 또는 rb 모드로 불러와야 한다                                                              
 pickle.dump(phone_book, outfile)                              # 윗 문장에서 연 outfile에 phone_book 데이터를 입력한다   
 print("주소들이 파일에 저장되었습니다")                       # 입력이 끝났으면 print함수를이용하여  "주소들이 파일에 저장되었습니다"  
 outfile.close()                                               # outfile을 닫는다.
def load():                                                    # load 함수를 정의한다
 infile = open("phonebook.dat", "rb")           # "phonebook.dat"파일을 rb형식으로 열어 infile에 저장한다 
 phone_book = pickle.load(infile)               # infile에 있는 자료를 불러온다
 infile.close()                                 # infile을 닫는다 
 print("파일에서 주소를 읽었습니다.")           # 이 과정의 실행이 끝났으면 print함수를 통해 "파일에서 주소를 읽었습니다."를 출력한다.
 go_first()   
def add():                                      # add함수를 정의내린다
 phone_book[nameEntry.get()] = phoneEntry.get()  
 print(phone_book)
 save()
def go_first():                     
 global current                     # 전역함수인 global 함수를 사용한다   
 current = 0                        # current값을 0으로 설정한다
 ks = list(phone_book)              # phone_book을 변수 ks에 저장한다
 print(phone_book)                  # phone_book을 print 함수를 이용하여 출력한다  
 nameEntry.delete(0, END)           # nameEntry에서 입력한  마지막 문자열을 삭제한다 
 nameEntry.insert(0, ks[current])   # nameEntry에서 입력한 기존의 전화번호부에 추가한다.
 phoneEntry.delete(0, END)         
 phoneEntry.insert(0, phone_book[ks[current]])
def go_next():               # 함수 go_next를 설정한다
 global current              # 전역함수 global을 사용한다
 current += 1                # current는 그전의 current값에 계속 1을 더해나가는 방식으로 정의내린다 
 ks = list(phone_book)
 nameEntry.delete(0, END)
 nameEntry.insert(0, ks[current])
 phoneEntry.delete(0, END)
 phoneEntry.insert(0, phone_book[ks[current]])
def go_previous():            # go_previous 함수는
 print("구현되지 않았음")     # print 함수를 이용하여 "구현되지 않았음"을 출력하고
def go_last():                # go_last 함수또한  
 print("구현되지 않았음")     # print 함수를 이용하여 "구현되지 않았음"을 출력하고
b1 = Button(frame3, text = "추가", command = add).grid(row = 1, column = 1)         # '추가'라고 쓰여있는 버튼의 위치 및 크기를  정의내려 변수 b1에 저장한다  
b2 = Button(frame3, text = "처음", command = go_first).grid(row = 1, column = 2)    # '처음'이라고 쓰여있는 버튼의 위치 및 크기를  정의내려 변수 b2에 저장한다 
b3 = Button(frame3, text = "다음", command = go_next).grid(row = 1, column = 3)     # '다음'이라고 쓰여있는 버튼의 위치 및 크기를  정의내려 변수 b3에 저장한다 
b4 = Button(frame3, text = "이전", command =go_previous).grid(row = 1, column = 4)  # '이전'이라고 쓰여있는 버튼의 위치 및 크기를  정의내려 변수 b4에 저장한다 
b5 = Button(frame3, text = "마지막", command = go_last).grid(row = 1, column = 5)   # '마지막'이라고 쓰여있는 버튼의 위치 및 크기를  정의내려 변수 b5에 저장한다 
b6 = Button(frame3, text = "파일 읽기", command = load).grid(row = 1, column = 6)   # '파일읽기'라고 쓰여있는 버튼의 위치 및 크기를  정의내려 변수 b6에 저장한다 
window.mainloop()                   
