# How do I get the text contents of a textarea with webdriver?
IWebElement element = ...
String returnText = ((IJavaScriptExecutor)webDriver).ExecuteScript("return arguments[0].innerHTML", element).ToString();