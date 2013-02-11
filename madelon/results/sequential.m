results = csvread( 'results2.csv' );

err = results(:,1);

best = err < 0.038;
good = err < 0.044;
mediocre = err < 0.05;
bad = err >= 0.05;

best_color = [ 217/255 71/255 1/255 ];
good_color = [ 253/255 141/255 60/255 ];
mediocre_color = [ 253/255 190/255 133/255 ];
bad_color = [ 254/255 237/255 222/255 ];

%{
best_color = [ 35/255 139/255 69/255 ];
good_color = [ 116/255 196/255 118/255 ];
mediocre_color = [ 186/255 228/255 179/255 ];
bad_color = [ 237/255 248/255 233/255 ];
%}

plot( results( bad, 2 ), results( bad, 3 ), 'o', 'Color', bad_color, 'MarkerFaceColor', bad_color )
hold on;

plot( results( mediocre, 2 ), results( mediocre, 3 ), 'o', 'Color', mediocre_color, 'MarkerFaceColor', mediocre_color )
plot( results( good, 2 ), results( good, 3 ), 'o', 'Color', good_color, 'MarkerFaceColor', good_color )
plot( results( best, 2 ), results( best, 3 ), 'o', 'Color', best_color, 'MarkerFaceColor', best_color )

xlabel( 'clusters')
ylabel( 'rbf gamma' )

hold off;

