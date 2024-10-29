// ----------------------------------------------------  TELEGRAM -----------------------------------------------------------------------
double chat_id[3] = {529408795, 561789930};
const string Token = "7681078661:AAFa53g5UjVga17KFHI1vJV0GxugrLeM08M";
const string URL = "https://api.telegram.org";

bool SendMessage(double id, string text) {
   
   char postData[];
   char resultData[];
   string resultHeaders;
   int response;
   
   string requestUrl = URL + "/bot" + Token + "/sendMessage?chat_id=" + id + "&text=" + text;
   response = WebRequest("POST", requestUrl, NULL, 1000, postData, resultData, resultHeaders);
   Print("Response > ",response);
   return (response == 200);
}


datetime lastRunTime;
double daily_loss, max_loss, target;
int x;

int OnInit() {

   daily_loss = NormalizeDouble(AccountEquity() - (AccountEquity() * 0.01 * 5), 2);
   max_loss = NormalizeDouble(AccountEquity() - (AccountEquity() * 0.01 * 12), 2);
   target = NormalizeDouble(AccountBalance() + (AccountBalance() * 0.01 * 8), 2);

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
      Print("Daily loss old ", daily_loss);
      lastRunTime = TimeCurrent();  // Update last run time
      daily_loss = NormalizeDouble(AccountInfoDouble(ACCOUNT_EQUITY) - (AccountInfoDouble(ACCOUNT_EQUITY) * 0.01 * 5), 2);
      Print("Daily loss new ", daily_loss);  // Call the function that should only run at 00:00
   }
}


void OnTick() {
   Comment("Working . . .", "\nDaily loss  ", daily_loss, "\nMax Drawdown  ", max_loss, "\nTarget  ", target);

   if (AccountEquity() < daily_loss) {
      Print("Daily loss done");
      for (x = 0; x < ArraySize(chat_id); x++) {
         SendMessage(chat_id[x], "Daily loss done   Time - " + TimeCurrent() + "   Name - " + AccountInfoString(ACCOUNT_NAME) + "   Login - " + AccountInfoInteger(ACCOUNT_LOGIN));
      }
      Write_loss();
   }
   else if (AccountEquity() < max_loss) {
      Print("Max Drawdown done");
      for (x = 0; x < ArraySize(chat_id); x++) {
         SendMessage(chat_id[x], "Max Drawdown done   Time - " + TimeCurrent() + "   Name - " + AccountInfoString(ACCOUNT_NAME) + "   Login - " + AccountInfoInteger(ACCOUNT_LOGIN));
      }
      Write_loss();
   }
   else if (AccountBalance() > target && OrdersTotal() == 0) {
      if (OrderSelect(OrdersHistoryTotal() -1 , SELECT_BY_POS, MODE_HISTORY) ) {
         if (OrderCloseTime() + 60 * 10 < TimeCurrent()) {
            for (x = 0; x < ArraySize(chat_id); x++) {
               SendMessage(chat_id[x], "Target done   Time - " + TimeCurrent() + "   Name - " + AccountInfoString(ACCOUNT_NAME) + "   Login - " + AccountInfoInteger(ACCOUNT_LOGIN));
            }
            Write_loss();
         }
      }
   }

}


void Write_loss() {
   while (true) {
      int handle = FileOpen("loss.csv", FILE_WRITE|FILE_CSV);
      if(handle != INVALID_HANDLE) {
         bool result = FileWrite(handle, 1111);
         if (result) {
            Print("File write successfull!");
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
