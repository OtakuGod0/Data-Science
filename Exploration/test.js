symbol = document.getElementById("symbol")
dob = document.getElementById("dob")
form = document.getElementsByName("neb"); form = form[0]
button = document.getElementsByName("submit"); button = button[0]
list = [
    22700559, 22700560, 22700561, 22700562, 22700563,
    22700564, 22700565, 22700566, 22700567, 22700568,
    22700569, 22700570, 22700571, 22700572, 22700573,
    22700574, 22700575, 22700576, 22700577, 22700578,
    22700579
  ]
  
for(i=0;i<list.length;i++){
    dob.value = "2063/11/10"
    symbol.value = list[i]
    if(validateForm()){
        button.click()
    }
}