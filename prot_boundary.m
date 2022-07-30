df = load('max_spread_pts.csv');
b = boundary(df(:,1),df(:,2));
dfnew = df(b,:);
% scatter(df(:,1),df(:,2),5)
% hold on
% plot(dfnew(:,1),dfnew(:,2),'LineWidth',2,'color','red')
dlmwrite('boundary3d.csv', dfnew, 'delimiter', ' ')