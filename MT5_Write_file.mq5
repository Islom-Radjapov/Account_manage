#include <Trade/Trade.mqh>
CTrade  trade;

// ----------------------------------------------------  TELEGRAM -----------------------------------------------------------------------
double chat_id[3] = {5294408795, 561789930};
const string Token = "7382465275:AAHMwFNC8mQWrYX0Bgkm8b9krQ3NLis-xPA";
const string URL = "https://api.telegram.org";

bool SendMessage(double id, string text) {
   
   char postData[];
   char resultData[];
   string resultHeaders;
   int response;
   
   string requestUrl = URL + "/bot" + Token + "/sendMessage?chat_id=" + id + "&text=" + text;
   response = WebRequest("POST", requestUrl, NULL, 1000, postData, resultData, resultHeaders);
   return (response == 200);
}


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
   if (PositionsTotal() == 0) {
      trade.Sell(1, _Symbol, SymbolInfoDouble(_Symbol, SYMBOL_BID));
   }
   
   if (AccountInfoDouble(ACCOUNT_EQUITY) < daily_loss) {
      Print("Daily loss done");
      for (int x = 0; x < ArraySize(chat_id); x++) {
         SendMessage(chat_id[x], "Daily loss done \nName  " + AccountInfoString(ACCOUNT_NAME) + "\nLogin  " + AccountInfoInteger(ACCOUNT_LOGIN));
      }
      Daily_loss();
   }
   else if (AccountInfoDouble(ACCOUNT_EQUITY) < max_loss) {
      Print("Max Drawdown done");
      for (int x = 0; x < ArraySize(chat_id); x++) {
         SendMessage(chat_id[x], "Max Drawdown done \nName  " + AccountInfoString(ACCOUNT_NAME) + "\nLogin  " + AccountInfoInteger(ACCOUNT_LOGIN));
      }
      Max_Drawdown();
   }

}


void Daily_loss() {
   while (true) {
      int handle = FileOpen("loss.csv", FILE_WRITE|FILE_CSV);
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
      int handle = FileOpen("loss.csv", FILE_WRITE|FILE_CSV);
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

