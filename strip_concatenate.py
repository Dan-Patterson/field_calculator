d e f   s t r i p _ c o n c a t e n a t e ( i n _ f l d s ,   s t r i p _ l i s t = [ "   " ,   " , " ,   N o n e ] ) :  
         " " " P r o v i d e   t h e   f i e l d s   a s   a   l i s t   i e   [ a ,   b ,   c ]   t o   s t r i p   s p a c e s  
         :   a n d   r e m o v e   n u l l s  
         :   u s e :   p y t h o n   p a r s e r  
         :   s y n t a x :   s t r i p _ s t u f f ( ' ! a ! ,   ! b ! ,   ! c ! ] )   a s s u m e d   f i e l d   n a m e s  
         " " "  
         f i x e d   =   [ ]  
         f m t   =   [ ]  
         f o r   i   i n   i n _ f l d s :  
                 i f   i   n o t   i n   s t r i p _ l i s t :  
                         f i x e d . a p p e n d ( i )  
                         f m t . a p p e n d ( " { } " )  
         f r m t   =   "   " . j o i n ( [ f   f o r   f   i n   f m t ] )  
         f r m t . s t r i p ( )          
         f l d s   =   [ s t r ( i ) . s t r i p ( )   f o r   i   i n   f i x e d ]  
         r e s u l t   =   f r m t . f o r m a t ( * f i x e d )  
         r e t u r n   r e s u l t  
 _ _ e s r i _ f i e l d _ c a l c u l a t o r _ s p l i t t e r _ _  
 s t r i p _ c o n c a t e n a t e ( ) 