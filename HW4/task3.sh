gawk -F',' '$3 == 2 && $13 == "S\r"{print}' titanic.csv | sed 's/female/F/g; s/male/M/g' | gawk -F',' '{if ($7 != "") {sum += $7 ; count++}} END { print "Average age: ", sum/count}{print}'
