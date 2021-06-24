class StockHolding{
    var purchaseSharePrice: Float 
    var currentSharePrice: Float
    var numberOfShares: Int
    var companyName: String
    //above are the instance variables of the class
    init(purchaseSharePrice:Float,currentSharePrice:Float,numberOfShares:Int,companyName:String){
        self.purchaseSharePrice=purchaseSharePrice
        self.currentSharePrice=currentSharePrice
        self.numberOfShares=numberOfShares
        self.companyName=companyName
    }
    //
    func costInDollars()-> Float{
        return purchaseSharePrice*Float(numberOfShares)
        //formulae for calculations
    }
    //instance method 1
    func valueInDollars()-> Float{
        return currentSharePrice*Float(numberOfShares)
        //formulae for calculations
    }
    //instance method 2
}

var ss1=StockHolding(purchaseSharePrice:5.0,currentSharePrice:10.0,numberOfShares:20,companyName:"Hello_Swift")
var ss2=StockHolding(purchaseSharePrice:10.0,currentSharePrice:15.0,numberOfShares:20,companyName:"Hello_Swift2")
var ss3=StockHolding(purchaseSharePrice:15.0,currentSharePrice:20.0,numberOfShares:20,companyName:"Hello_Swift3")
//the above are the 3 instances created
var stocks: [StockHolding]=[ss1,ss2,ss3]
//array of StockHolding instances

stocks.sort{
    $0.companyName < $1.companyName
}
//Sorting the array alphabetically

for item in stocks{
    print(item.companyName)
    print(item.purchaseSharePrice)
    print(item.currentSharePrice)
    print(item.numberOfShares)
    print(item.costInDollars())
    print(item.valueInDollars())
}