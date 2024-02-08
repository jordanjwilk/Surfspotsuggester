def suggest(swell_direction):
  suggest_side = {
    "north" : "northshore",
    "northwest" : "northshore",
    "northeast" : "northshore", 
    "south" : "southshore",
    "southwest" : "southshore",
    "southeast" : "southshore",
    "west" : "westside",
    "east" : "eastside"
  }

  return suggest_side.get(swell_direction.lower(), "uknown")

swell_direction = "north"
suggested_side = suggest(swell_direction)
print("A huge swell is coming from the", swell_direction, "go check out the", suggested_side)
