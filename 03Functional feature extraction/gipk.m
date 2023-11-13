function [result_circ,result_dis]=gipk(nc,nd,inter)
% compute Gaussian interaction profile kernel
%	Inputs:
%		nc: the number of circRNAs
%		nd:	the number of diseases
%		inter: an nc*nd association matrix between circRNAs and diseases
%
%	Outputs:
%		result_circ: Gaussian interaction profile kernel of circRNAs
%		result_dis: Gaussian interaction profile kernel of diseases

normSum=0;
    for i=1:nc  
        normSum = normSum + norm(inter(i,:))^2 
    end
    gamal=1/(normSum/nc);
    [pkl]=zeros(nc,nc);
    for i=1:nc
        for j=1:nc
            pkl(i,j)=exp(-gamal*(norm(inter(i,:)-inter(j,:)))^2); 
        end
    end  
    
    %%disease
    normSum=0;
    for i=1:nd
        normSum = normSum + norm(inter(:,i))^2;
    end
    gamad=1/(normSum/nd);
    [pkd]=zeros(nd,nd);
    for i=1:nd
        for j=1:nd
            pkd(i,j)=exp(-gamad*(norm(inter(:,i)-inter(:,j)))^2);
        end
    end 
    result_circ=pkl;
    result_dis=pkd;
    
end