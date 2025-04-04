from app import db

class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    creators = db.Column(db.String)
    image = db.Column(db.String)
    audio = db.Column(db.String)

    melody_battle_id = db.Column(db.Integer, db.ForeignKey('melody_battle.id'), nullable=False)
    melody_battle = db.relationship('MelodyBattle', backref=db.backref('tracks', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'creators': self.creators,
            'image': self.image,
            'audio': self.audio
        }