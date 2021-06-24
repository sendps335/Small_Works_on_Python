class StockHolding{
    var purchaseSharePrice: Float 
    var currentSharePrice: Float
    var numberOfShares: Int
    var companyName: String
    var conversionRate: Float
    //above are the instance variables of the class
    init(purchaseSharePrice:Float,currentSharePrice:Float,numberOfShares:Int,companyName:String,conversionRate:Float=1.0){
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
    func disp(){
        print("purchase \(purchaseSharePrice)")
        print("current \(currentSharePrice)")
        print("Share \(numberOfShares)")
        print("company \(companyName)")
    }
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

var numstock:Int?
print("Enter the No of Stock Holding You want to show(Max 8)")
//Take the numbers of different stocks as user input
numstock=Int(readLine()!)
if(numstock != nil){ //checkk whether it is null or not
    var stocks:[StockHolding]=[]
    var i:Int
    i=0
    while(i < numstock){
        var purchaseSharePrice:Float
        var currentSharePrice:Float
        var numberOfShares:Int
        var companyName:String
        print("Enter the constraints of the class")
        //input of constraints
        purchaseSharePrice=Float(readLine()!)
        currentSharePrice=Float(readLine()!)
        numberOfShares=Int(readLine()!)
        companyName=readLine()!
        let ss=StockHolding(purchaseSharePrice:purchaseSharePrice,currentSharePrice:currentSharePrice,numberOfShares:numberOfShares,companyName:companyName)
        stocks.append(ss)
        //append
        i=i+1
    }
    var choice:Int?
    print("Enter 1-6 as per the requirements of the Program and 7 to terminate it")
    choice=Int(readLine()!)
    if(choice != nil){
    if(choice==1){
        stocks.sort{
            $0.valueInDollars() < $1.valueInDollars()
        }
        //List Stock Value
        stocks[0].disp()
    }
    else if(choice==2){
        stocks.sort{
            $0.valueInDollars() > $1.valueInDollars()
        }
        //List Stock Value
        stocks[0].disp()
    }
    else if(choice==3){
        stocks.sort{
            $0.valueInDollars()-$0.costInDollars() < $1.valueInDollars()-$0.costInDollars()
        }
        stocks[0].disp()
    }
    else if(choice==4){
        stocks.sort{
            $0.valueInDollars()-$0.costInDollars() > $1.valueInDollars()-$0.costInDollars()
        }
        stocks[0].disp()
    }
    else if(choice==5){
        stocks.sort{
            $0.companyName < $1.companyName
        }
        stocks[0].disp()
    }
    else if(choice==6){
        stocks.sort{
            $0.valueInDollars() < $1.valueInDollars()
        }
        for i in stocks{
            i.disp()
        }
    }
    else{
        print("Thanks for using our application")
    }
    }
    else{
        print("Wrong Choice")
    }
}
else{
    print("Null Input is Given")
}