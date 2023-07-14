from random import randint


hand_img = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''',
    '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    ''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    '''
]

hand_text = ['rock', 'paper', 'scissors']


def get_random_hand():
    index = randint(0, 2)
    return {
        'text': hand_text[index],
        'img': hand_img[index]
    }


def get_hand_img(index):
    return hand_img[index]
