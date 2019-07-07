import pygame, sys, time
pygame.init()

size = width, height = 500, 200
background_color = (54,137,209)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('GetUpTimer')
pygame.display.set_icon(pygame.image.load('Icon.png'))

one_period_time = 2700 # in seconds
timer_start = 0.0
timer_stop = 0.0

my_font = pygame.font.SysFont('My Font', 100)
displayed_time = my_font.render('00:00:00', True, (0,0,0))


# Changes seconds into hours, minutes and seconds and returns it as a single string
def format_time(time_in_seconds):
    hours = int(time_in_seconds / 3600).__str__()
    time_in_seconds -= int(hours) * 3600
    minutes = int(time_in_seconds / 60).__str__()
    time_in_seconds -= int(minutes) * 60
    if minutes.__len__() == 1:
        minutes = '0' + minutes
    seconds = time_in_seconds.__str__()
    if seconds.__len__() == 1:
        seconds = '0' + seconds
    return '{}:{}:{}'.format(hours, minutes, seconds)


def set_position_of_timer(text):
    size = my_font.size(text)
    pos_width = (width / 2) - (size[0] / 2)
    pos_height = (height / 2) - (size[1] / 2)
    return (pos_width, pos_height)


time_position = set_position_of_timer('0:00:00')


def update_screen():
    screen.fill(background_color)
    screen.blit(displayed_time, time_position)
    pygame.display.flip()


def check_for_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


# plays alarm for 1 minute unless user turns it off.
# After that program waits for 5 minutes unless user decides otherwise
def play_alarm():
    alarm_volume = 0.05
    alarm_length = 60
    break_length = 300

    alarm_sound = pygame.mixer.Sound('Alarm1.wav')
    alarm_sound.set_volume(alarm_volume)
    alarm_sound.play(-1)

    timer_start = time.time()
    while True:
        check_for_events()
        timer_stop = time.time()
        if timer_stop - timer_start > alarm_length:
            alarm_sound.stop()
            break
        else:
            time.sleep(0.3)

    timer_start = time.time()
    while True:
        check_for_events()
        timer_stop = time.time()
        if timer_stop - timer_start > break_length:
            break
        else:
            time.sleep(0.3)


while True:
    timer_start = time.time()
    current_time = 0
    while timer_stop - timer_start < one_period_time:
        check_for_events()

        timer_stop = time.time()
        rounded_time = int(timer_stop - timer_start)
        if rounded_time > current_time:
            current_time = rounded_time

            formatted_time = format_time(one_period_time - current_time)
            displayed_time = my_font.render(formatted_time, True, (0,0,0))

            update_screen()
        else:
            time.sleep(0.2)
    play_alarm()
