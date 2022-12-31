<h1>Auctions</h1>
<p>Welcome to the auctions project! This project allows users to enter their bids for an auction and determines the highest bidder at the end.</p>
<h2>Getting Started</h2>
<p>To get started, clone this repository and run the code in your preferred Python environment. Make sure to have the <code>replit</code> and <code>art</code> modules installed.</p>
<h2>Code Overview</h2>
<p>The code begins by importing the <code>clear</code> function from <code>replit</code> and the <code>logo</code> ASCII art from the <code>art</code> module. The logo is then printed to the console.</p>
<p>Next, a variable <code>more_bidders</code> is created and set to <code>False</code> and an empty dictionary <code>all_bid</code> is created to store all of the bids.</p>
<p>The <code>find_highest_bidder()</code> function is defined to determine the highest bidder by taking in the <code>bidding_record</code> dictionary as an argument. It iterates through the dictionary and compares the values (bid amounts) to determine the highest bid. The winner is then printed to the console.</p>
<p>A while loop is created to continue running until <code>more_bidders</code> becomes <code>True</code>. Inside the loop, the user is prompted for their name and bid amount. These values are then added to the <code>all_bid</code> dictionary. The user is then asked if there are more bidders. If the answer is "yes", the loop continues and the screen is cleared using the <code>clear()</code> function. If the answer is "no", <code>more_bidders</code> is set to <code>True</code> and the <code>find_highest_bidder()</code> function is called with the <code>all_bid</code> dictionary as an argument to determine the highest bidder.</p>
<h2>Using the Code</h2>
<p>To use the code, simply run it in your Python environment and follow the prompts in the console. Enter your name and bid amount when prompted, and when there are no more bidders, the highest bidder will be determined and printed to the console.</p>
<h2>Contributing</h2>
<p>If you would like to contribute to this project, please fork the repository and make your changes. Submit a pull request and we can discuss the changes further.</p>
<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>


