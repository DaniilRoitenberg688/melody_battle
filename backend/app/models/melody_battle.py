from app import db

class MelodyBattle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    play_list_url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('melody_battles', lazy=True))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'play_list_url': self.play_list_url,
            'user': self.user.as_dict()
        }
