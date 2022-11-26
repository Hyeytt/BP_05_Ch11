import pickle                                 # 리스트나 클래스 이외의 자료형은 일반적인 파일 입출력방법으로는 데이터를 저장 또는 불러올 수 없다. 텍스트 이외의 자료형을 파일로 저장하기 위해
                                              # 라이브러리에서 pickle 모듈을 불러온다 
outfile = open("test.dat", "wb")              # wb 모드로 "test.dat"파일을 불러와 변수 outfile에 저장한다
                                              # pickle로 데이터를 저장하거나 불러올때는 파일을 바이트 형식인  wb 또는 rb 모드로 불러와야 한다
pickle.dump(12, outfile)                      # test.dat에 13를 입력한다
pickle.dump(3.14, outfile)                    # test.dat에 3.14를 입력한다
pickle.dump([1, 2, 3, 4, 5], outfile)         # test.dat에[1, 2, 3, 4, 5] 를 입력한다  
outfile.close()                               # 파일을 닫는다
infile = open("test.dat", "rb")               # test.dat파일을 열어 변수 infile에 저장한다.
print(pickle.load(infile))                    # infile에서 객체를를 불러온다       
print(pickle.load(infile))
print(pickle.load(infile))
infile.close()                                # infile을 닫는다 
