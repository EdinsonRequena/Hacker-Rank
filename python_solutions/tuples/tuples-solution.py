def main(n, input_list):
    for i in range(n):
        input_list[i] = int(input_list[i])
    t = tuple(input_list)
    print(hash(t))

if __name__ == '__main__':
    n = int(input())
    input_list = map(int, input().split())

    main(n, input_list)