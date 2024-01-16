import random 
#### controller
class LottoController:  # 로또 컨트롤러
    def __init__(self, name):
        self.name=name

    def play(self):  # play 과정을 정하는 함수
        reader=Reader()
        coin=5

        while True:
            get_number=Get_Number(self.name)
            tnumber=get_number.get_number_selection()
            inumber=reader.input_number()
            decision = Decision(self.name, tnumber, inumber,coin)
            decision.results()
            coin=decision.coin
            
            print("정답 숫자 ", decision._tnumber, ", 입력 숫자 ", \
              decision._inumber, ", 맞춘 개수 ", decision._count, "개")
            if not reader.ox("{0}님(점수:{1}) 계속 하시겠습니까? 계속(1번)/그만(0번)".format(self.name,coin)):
                print("Exit!")
                break

#### model
class Get_Number:  # 로또 번호를 가져오는 클래스
    def __init__(self, name):
        self.name=name

    def get_number_selection(self):  # 랜덤 번호가 담긴 리스트 생성 함수
        numbers=[random.randint(1,15) for _ in range(3)]
        
        return numbers

class Decision:  # 결과 결정하는 클래스
    def __init__(self, name, tnumber, inumber, coin):
        self.name=name
        self._tnumber=tnumber
        self._inumber=inumber
        self._coin=coin

    @property
    def tnumber(self):  #로또 번호 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self._tnumber

    @property
    def inumber(self):  #참가자가 작성한 번호 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self._inumber

    @property
    def coin(self):  #현재 코인 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self._coin

    @property
    def count(self):  #몇 개 맞췄는지에 대한 카운트 리턴하는 함수, return 뒤에 올 코드를 완성하시오.
        return self._count

    def results(self):  #입력한 번호와 로또 번호가 몇 개 일치하는지 계산하는 함수
        tnumber=self._tnumber
        inumber=self._inumber.copy()
        count=0

        def isin(olist,target):
            while olist:
                if olist[0] == target:
                    return True
                else:
                    olist=olist[1:]
            else:
                return False
            
        for t in tnumber:
            if isin(inumber,t):
                count+=1
                inumber.remove(t)
        self._count=count

        if self._count==3:
            self.coin+=5
        elif self._count==2:
            self._coin+=3
        else:
            self._coin-=1

class Reader:  #참가자 입력정보 클래스
    @staticmethod
    def get_name():  #참가자 이름 입력 받아오는 함수, return 뒤에 올 코드를 완성하시오.
        return input("플레이어의 이름을 입력하세요:")

    @staticmethod
    def ox(message):  #참가자가 계속할건지 종료할건지 리턴하는 함수
        res=int(input(message))
        if res==1:
            return True
        else:
            return False

    @staticmethod
    def input_number():  #참가자가 입력하는 번호를 리스트로 리턴하는 함수
        numbers=[]
        for i in range(1,4):
            a=input(str(i)+"번째 숫자 입력")
            numbers.append(int(a))
        return numbers


#### main
######## do not edit here ########
def main():
    reader = Reader()
    name = reader.get_name()

    lottocontroller = LottoController(name)
    lottocontroller.play()

if __name__ == "__main__":
    main()
