def tile_cost(width, height, cost)
  width * height * cost
end

print "\nTile cost Calculator \n"
print "\nEnter height: "
height = gets.strip.to_i
print "\nEnter width: "
width = gets.strip.to_i
print "\nPrice per square: "
cost = gets.strip.to_i
total_cost = tile_cost(width, height, cost)
printf("\nTotal cost: $%.2f\n\n", total_cost)