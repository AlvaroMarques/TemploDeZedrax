extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	$Button.connect("pressed",self,"_on_Button_pressed")
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button_pressed():
	print("oi")
	get_tree().change_scene("res://xadrez.tscn")
	pass # Replace with function body.