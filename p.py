def kanish__(arr,target):
    steps=0
    for i in range(len(arr)):
        steps+=1
        if arr[i]==target:
            print("found after",steps,"steps")
            return
        print("not found after",steps,"steps")
arr=[10,20,30,40,50]
kanish__(arr ,10)
kanish__(arr,50)
kanish__(arr,90)