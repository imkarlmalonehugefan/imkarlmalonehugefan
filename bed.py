import random
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0

for fin in range(365):
    sleep_time = random.randint(1, 12)
    if sleep_time == 1:
        a = a + 1
    if sleep_time == 2:
        b = b + 1
    if sleep_time == 3:
        c = c + 1
    if sleep_time == 4:
        d = d + 1
    if sleep_time == 5:
        e = e + 1
    if sleep_time == 6:
        f = f + 1
    if sleep_time == 7:
        g = g + 1
    if sleep_time == 8:
        h = h + 1
    if sleep_time == 9:
        i = i + 1
    if sleep_time == 10:
        j = j + 1
    if sleep_time == 11:
        k = k + 1
    if sleep_time == 12:
        l = l + 1
   
sleep_average_list = [a, b, c, d, e, f, g, h, i, j, k, l]
print(sleep_average_list)
while True:
    q = int(input('what time do you go to bed?(just number)'))
    if q>=10:
        print('Damn!! Me too! i think you are my destiny! aren\'t you?\n thus i guess we should marry each other')

    else:
        print('damn, move out my way! why do you go to bed so early Boy/')