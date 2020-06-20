import pyautogui

pyautogui.click()
distance=400
while distance>0:
    print(distance,0)
    pyautogui.dragRel(distance,0,duration=1.5)
    distance=distance-25
    print(0,distance)
    pyautogui.dragRel(0,distance,duration=1.5)
    distance=distance-25
    print(-distance,0)
    pyautogui.dragRel(-distance,0,duration=1.5)
    distance=distance-25
    print(0,-distance)
    pyautogui.dragRel(0,-distance,duration=1.5)
    distance=distance-25

