#include <Trade/Trade.mqh>
CTrade  trade;


datetime lastRunTime;
double daily_loss, max_loss;

int OnInit() {
   
   EventSetTimer(60); // Timer in seconds (60 seconds = 1 minute)
   lastRunTime = 0;   // Initialize lastRunTime (can load from file or variable storage)
   
   
   daily_loss = NormalizeDouble(AccountInfoDouble(ACCOUNT_EQUITY) - (AccountInfoDouble(ACCOUNT_EQUITY) * 0.01 * 5), 2);
   max_loss = NormalizeDouble(AccountInfoDouble(ACCOUNT_EQUITY) - (AccountInfoDouble(ACCOUNT_EQUITY) * 0.01 * 12), 2);

   return (INIT_SUCCEEDED);
}


void OnDeinit(const int reason) {
   Comment("");
   EventKillTimer();  // Remove the timer when the expert is removed
}


void OnTimer() {
   MqlDateTime time1, time2;
   //datetime currentTime = TimeCurrent();
   TimeToStruct(TimeCurrent(), time1);
   TimeToStruct(lastRunTime, time2);

   // Check if the current time is after midnight and it hasn't run today
   if (time1.hour == 3 && time1.min == 0 && time1.day != time2.day) {
      
      lastRunTime = TimeCurrent();  // Update last run time
      daily_loss = NormalizeDouble(AccountInfoDouble(ACCOUNT_EQUITY) - (AccountInfoDouble(ACCOUNT_EQUITY) * 0.01 * 5), 2);
      Print(">>>>>>>>>>>>>>>>> 00:00  daily loss  ", daily_loss);  // Call the function that should only run at 00:00
   }
}



void OnTick() {
   
   Comment("Working . . .", "\nDaily loss  ", daily_loss, "\nMax Drawdown  ", max_loss);
   if (OrdersTotal() == 0) {
      trade.Sell(1, _Symbol, SymbolInfoDouble(_Symbol, SYMBOL_BID));
   }
   if (AccountInfoDouble(ACCOUNT_EQUITY) < daily_loss) {
      Print("Daily loss done");
      Daily_loss();
   }
   else if (AccountInfoDouble(ACCOUNT_EQUITY) < max_loss) {
      Print("Max Drawdown done");
      Max_Drawdown();
   }

}


void Daily_loss() {
   while (true) {
      int handle = FileOpen("daily_loss.csv", FILE_WRITE|FILE_CSV);
      if(handle != INVALID_HANDLE) {
         bool result = FileWrite(handle, 111);
         if (result) {
            Print("File write successful!");
            FileClose(handle);
            ExpertRemove();
            break;
         } else {
            Print("File write failed!");
         }
      } else {
         Print("Failed to open file!");
      }
      FileClose(handle);
      Sleep(5000);
   }
}


void Max_Drawdown() {
   while (true) {
      int handle = FileOpen("max_loss.csv", FILE_WRITE|FILE_CSV);
      if(handle != INVALID_HANDLE) {
         bool result = FileWrite(handle, 222);
         if (result) {
            Print("File write successful!");
            FileClose(handle);
            ExpertRemove();
            break;
         } else {
            Print("File write failed!");
         }
      } else {
         Print("Failed to open file!");
      }
      FileClose(handle);
      Sleep(5000);
   }
}