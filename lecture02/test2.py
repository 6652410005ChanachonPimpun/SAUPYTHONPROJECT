score = 50
print("Hello...", 5, True, 1.1, 1+1, "Hi....", score)

print("Hello..." + str(5) + str(True) + str(1.1) + str(1+1) + "Hi...." + str(score))# +

print("Hello... {} {} {} {} Hi.... {}".format(5, True, 1.1, 1+1,score))# เมธอด format 

print(f"Hello... {5} {True} {1.1} {1+1} Hi.... {score}")# f-string

print('Hello... %d %f Hi...'%(5, 25.5))# modular operator %