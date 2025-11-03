from CSWatch import CSWatch

cswatch = CSWatch()
id = cswatch.resolve_player_id("dis1ik3")
print(id)
score = cswatch.get_trust_score("https://steamcommunity.com/id/PIPE2223/")
print(score)