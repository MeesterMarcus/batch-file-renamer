import os

print('What number do you want to start with?')
counter = int(input())

for filename in os.listdir(os.getcwd()):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        extension = os.path.splitext(filename)[1]
        print(filename + ' changed to: ' + 'IMG-' + str(counter) + extension)
        os.rename(filename, 'IMG-' + str(counter) + extension)
        counter += 1

