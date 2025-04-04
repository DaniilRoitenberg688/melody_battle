from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    battle_id = db.Column(db.Integer, db.ForeignKey('melody_battle.id'), nullable=False)
    battle = db.relationship('MelodyBattle', backref=db.backref('players', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'battle': self.battle.as_dict()
        }
