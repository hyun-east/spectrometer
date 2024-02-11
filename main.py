import cv2

base = cv2.imread('base.png')[155:225, 190:306]
r01none = cv2.imread('r0.1none.png')[155:225, 190:306]
r01big = cv2.imread('r0.1big.png')[155:225, 190:306]
r01mid = cv2.imread('r0.1mid.png')[155:225, 190:306]
r01small = cv2.imread('r0.1small.png')[155:225, 190:306]
r005none = cv2.imread('r0.05none.png')[155:225, 190:306]
r005big = cv2.imread('r0.05big.png')[155:225, 190:306]
r005mid = cv2.imread('r0.05mid.png')[155:225, 190:306]
r005small = cv2.imread('r0.05small.png')[155:225, 190:306]
y01none = cv2.imread('y0.1none.png')[155:225, 190:306]
y01big = cv2.imread('y0.1big.png')[155:225, 190:306]
y01mid = cv2.imread('y0.1mid.png')[155:225, 190:306]
y01small = cv2.imread('y0.1small.png')[155:225, 190:306]
y005none = cv2.imread('y0.05none.png')[155:225, 190:306]
y005big = cv2.imread('y0.05big.png')[155:225, 190:306]
y005mid = cv2.imread('y0.05mid.png')[155:225, 190:306]
y005small = cv2.imread('y0.05small.png')[155:225, 190:306]
#[0:70, 0:115]


for i in range(115):
    img=base
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img2=base
    v=cv2.split(img[0:70, i])
    x=0
    for k in range(70):
        x += v[0][k][0]
    y = x/70
    print(y)

cv2.imshow('base', img2[0:70, 0:115])
cv2.imshow('base(gray)', img[0:70, 0:115])
cv2.waitKey(0)
