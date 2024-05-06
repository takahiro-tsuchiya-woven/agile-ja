import copy
# ----これらの関数を変更する必要はありません----

names = ["Nick", "Lewis", "Nikos"]

def contains(name, list_of_names):
    if name not in list_of_names:
        return False
    else:
        return True

def get_name(name, list_of_names):
    if name in list_of_names:
        return name
    else:
        return -1

def add_name(name, list_of_names):
    list_of_names.append(name)
    return name

def add_two(num):
    return num + 2

def divide_by_two(num):
    return num / 2

def greeting(name, num):
    message = f"Hello, {name}. It is {num} degrees warmer today than yesterday"
    print(message)
    return message

# ----ここにコードを書いてください----*/
# ----難易度: 富士----

# `my_assert` をここに定義し、以降のテストに使用してください。
def my_assert(expr, msg="Error"):
    if expr is False:
        return msg

# `contains` 用のテスト `test_contains` を作成してください
def test_contains():
    print(my_assert(contains("Nick", names), "Nick should be in the list."))
    print(my_assert(not contains("Alice", names), "Alice should not be in the list"))

# `add_name` 用のテスト `test_add_name` を作成してください
def test_add_name():
    test_names = copy.deepcopy(names)
    add_name("Alice", test_names)
    print(my_assert(len(test_names) == 4, "リストには4つの名前が含まれているはずです。"))
    print(my_assert(contains("Alice", test_names), "リストにAliceを追加したので、リストに存在するはずです。"))

# `add_two` 用のテスト `test_add_two` を作成してください
def test_add_two():
    print(my_assert(add_two(1) == 3, "1+2=3を期待しています。"))
    print(my_assert(add_two(-3) == -1, "-3+2=-1を期待しています。"))

# `divide_by_two` 用のテスト `test_divide_by_two` を作成してください
def test_divide_by_two():
    print(my_assert(divide_by_two(2) == 1, "2/2=1を期待しています。"))
    print(my_assert(divide_by_two(-4) == -2, "-4/2=-2を期待しています"))
    print(my_assert(divide_by_two(5.2) == 2.6, "5.2/2=2.6を期待しています。"))

# `greeting` 用のテスト `test_greeting` を作成してください
def test_greeting():
    expr_res = "Hello, Nick. It is 3 degrees warmer today than yesterday"
    print(my_assert(greeting("Nick", 3) == expr_res, "greeting is incorrect."))

test_contains()
test_add_name()
test_add_two()
test_divide_by_two()
test_greeting()


# ----難易度: キリマンジャロ----

# `my_assert` 用のテスト `test_my_assert_false` を作成し、式がFalseと評価されたときに指定したオプションの `msg` を適切に返すかどうかをチェックしてください。
def test_my_assert_false():
    print(my_assert(my_assert(False, "my_assertのエラーチェック") == "my_assertのエラーチェック", "my_assertのmsgが不正です。"))
    print(my_assert(my_assert(False) == "Error", "my_assertのmsgが不正です。"))

test_my_assert_false()