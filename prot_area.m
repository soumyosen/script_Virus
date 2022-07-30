df = load('pts_mem.txt');
df(:,3) = round(df(:,3),1);
%TF = ismatrix(df);
%disp(TF)
z = unique(df(:,3));
arealist = [];

for i = 1 : length(z)
    df1 = df(df(:,3) == z(i),:);
    %df1
    b = boundary(df1(:,1),df1(:,2));
    df1new = df1(b,:);
    area = polyarea(df1new(:,1),df1new(:,2));
    %disp(area);
    arealist(i) = area;    
end

% plot(z, arealist)
% title('Area of Dimer of Hetero-dimer of Zika Virus Envelope Protein')
% xlabel('zheight ($\AA$)','Fontsize',20,'Interpreter','latex','Fontname','TimesNewRoman')
% ylabel('Area ($\AA^{2}$)','Fontsize',20,'Interpreter','latex','Fontname','TimesNewRoman')
% grid on

newdf = [z transpose(arealist)];
dlmwrite('prot_area.csv', newdf, 'delimiter', ' ')
%size(z)
%size(arealist)