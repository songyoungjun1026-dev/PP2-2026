def main():
    cir, count= map(int,input("피자의 둘레와 개수를 입력하시오 (예:10,20) : ").split(','))
    area = cir*3.14**2
    all_area = area*count
    print(f"피자의 개수 : {count}개, 피자의 면적 : {area}, 피자의 총 면적 : {all_area}")
if __name__ == "__main__":
    main()
