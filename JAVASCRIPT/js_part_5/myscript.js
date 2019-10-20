function sleepIn(weekday, vacation) {
  return vacation || !weekday;
}

function monkeyTrouble(aSmile, bSmile) {
  return aSmile == bSmile;
}


function stringTimes(str, n) {
  var ret = '';
  var i = 0;
  while (i<n) {
    ret +=str;
    i++;
  }
  return ret
}

function luckySum(a, b, c){
  var ret = 0;
  if (a == 13){
    return ret;
  }
  ret +=a;
  if (b==13) {
    return ret;
  }
  ret += b;
  if (c==13) {
    return ret
  }
  ret += c;
  return ret
}

function caught_speeding(speed, is_birthday){
  var low_limit = 61;
  var medium_limit = 81;
  if (is_birthday) {
    low_limit += 5;
    medium_limit += 5;
  }
  if (speed<low_limit) {
    return 0;
  }
  if (speed<medium_limit) {
    return 1;
  }
  return 2;
}
function makeBricks(small, big, goal){
  return goal/big == 5 || goal%5 == small
}
