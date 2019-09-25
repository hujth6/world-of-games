from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    try:
        scores_file = open(SCORES_FILE_NAME, 'r')
        new_score = int(scores_file.read()) + POINTS_OF_WINNING
    except:
        new_score = POINTS_OF_WINNING
    finally:
        scores_file = open(SCORES_FILE_NAME, 'w')
        scores_file.write(str(new_score))
        scores_file.close()



