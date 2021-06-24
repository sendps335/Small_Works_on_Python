class StockHolding{
    var purchaseSharePrice: Float 
    var currentSharePrice: Float
    var numberOfShares: Int
    var companyName: String
    var conversionRate: Float
    //above are the instance variables of the class
    init(purchaseSharePrice:Float,currentSharePrice:Float,numberOfShares:Int,companyName:String,conversionRate:Float){
        self.purchaseSharePrice=purchaseSharePrice
        self.currentSharePrice=currentSharePrice
        self.numberOfShares=numberOfShares
        self.companyName=companyName
        self.conversionRate=conversionRate
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
//Inheritance of class to be done
class ForeignStockHolding:StockHolding{
    override init(purchaseSharePrice:Float,currentSharePrice:Float,numberOfShares:Int,companyName:String,conversionRate:Float){
        super.init(purchaseSharePrice:purchaseSharePrice,currentSharePrice:currentSharePrice,numberOfShares:numberOfShares,companyName:companyName,conversionRate:conversionRate)
    }
    //init() function
    override func costInDollars()->Float{
        return conversionRate*purchaseSharePrice*Float(numberOfShares)
    }
    override func valueInDollars()->Float{
        return conversionRate*currentSharePrice*Float(numberOfShares)
    }
}

var ss1=ForeignStockHolding(purchaseSharePrice:5.0,currentSharePrice:10.0,numberOfShares:20,companyName:"Hello_Swift",conversionRate:1.22)
var ss2=ForeignStockHolding(purchaseSharePrice:10.0,currentSharePrice:15.0,numberOfShares:20,companyName:"Hello_Swift2",conversionRate:1.22)
//conversionRate for canadian dollar is 1.22
//the above are the 3 instances created
var stocks: [StockHolding]=[ss1,ss2]
//array of StockHolding instances

stocks.sort{
    $0.companyName > $1.companyName
}
//Sorting the array alphabetically in reverse order

for item in stocks{
    print(item.companyName)
    print(item.purchaseSharePrice)
    print(item.currentSharePrice)
    print(item.numberOfShares)
    print(item.costInDollars())
    print(item.valueInDollars())
}