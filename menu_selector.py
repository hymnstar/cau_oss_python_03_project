import file_manager
import parking_spot_manager

def start_process(path):
    # 파일에서 문자열 리스트를 가져온다
    str_list = file_manager.read_file(path)
    # 문자열 리스트를 parking_spot 객체 리스트로 변환한다
    spots = parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))

        if select == 1:
            # parking_spot 객체 리스트를 출력한다
            parking_spot_manager.print_spots(spots)

        elif select == 2:
            # 필터 기능 
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                # 이름 추가
            elif select == 2:
                keyword = input('type city:')
                # 도시 추가
            elif select == 3:
                keyword = input('type district:')
                # 지역구 추가
            elif select == 4:
                keyword = input('type ptype:')
                # 타입 추가
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                # 위치 추가
            else:
                print("invalid input")

        elif select == 3:
            # 정렬 기능 
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            # 정렬 관련 코드 추가

        elif select == 4:
            # 프로그램 종료
            print("Exit")
            break

        else:
            print("invalid input")

