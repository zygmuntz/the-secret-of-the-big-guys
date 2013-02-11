results = csvread( 'results2.csv' );

err = results(:,1);

% arbitrarily chosen values
red = err < 0.038;
green = err < 0.044;
blue = err < 0.05;
black = err >= 0.05;

plot( results( black, 2 ), results( black, 3 ), 'ko' )
hold on;

plot( results( blue, 2 ), results( blue, 3 ), 'bo' )
plot( results( green, 2 ), results( green, 3 ), 'go' )
plot( results( red, 2 ), results( red, 3 ), 'ro' )

xlabel( 'clusters')
ylabel( 'selected_clusters' )

hold off;

