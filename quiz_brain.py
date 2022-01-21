class QuizBrain:

    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        cur_q = self.question_list[self.question_num]
        self.question_num += 1
        player_ans = input(f"Q.{self.question_num} {cur_q.text} (True/False)? ")
        self.check_ans(player_ans, cur_q.answer)

    def shq(self):
        return self.question_num < len(self.question_list)

    def check_ans(self, user_ans, cor_ans):
        if use






