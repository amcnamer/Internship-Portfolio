// Fill out your copyright notice in the Description page of Project Settings.


#include "WeaponItem.h"
#include "CharacterStatComponent.h"

UWeaponItem::UWeaponItem()
	:weaponDamage(0.0f),weaponRange(0.0f),armorPierce(0.0f),damageType(ItemDamageType::UNINITIALIZED)
{
}

void UWeaponItem::Set(const int _maxStackSize, const int _currentStackSize, const float _weight, const float _currencyCost, FString _itemName, 
	CharacterItemType _itemType, CharacterItemTier _itemTier, const float _weaponDamage, const float _weaponRange, const float _armorPierce, 
	ItemDamageType _damageType, WeaponType _weaponType)
{
	this->maxStackSize = _maxStackSize;
	this->currentStackSize = _currentStackSize;
	this->weight = _weight;
	this->currencyCost = _currencyCost;
	this->itemName = _itemName;
	this->itemType = _itemType;
	this->itemTier = _itemTier;
	this->weaponDamage = _weaponDamage;
	this->weaponRange = _weaponRange;
	this->armorPierce = _armorPierce;
	this->damageType = _damageType;
	this->weaponType = _weaponType;
}





void UWeaponItem::Attack(AActor* actor) const
{
	UCharacterStatComponent* StatComp = actor->FindComponentByClass<UCharacterStatComponent>();
	if (StatComp)
	{
		//TODO:  add actor equipment component with armor value for character defense value, 
		// then combine that value and armor pierce value for damage roll.

		StatComp->Adjust(this->GetWeaponDamage(), CharStatName::HEALTH);

		//clean up for disposal
		StatComp = nullptr;
	}
}

float UWeaponItem::GetWeaponDamage() const
{
	return this->weaponDamage * -1;
}

float UWeaponItem::GetWeaponRange() const
{
	return this->weaponRange;
}

float UWeaponItem::GetWeaponPierce() const
{
	return this->armorPierce;
}

ItemDamageType UWeaponItem::GetWeaponDamageType() const
{
	return this->damageType;
}

WeaponType UWeaponItem::GetWeaponType() const
{
	return this->weaponType;
}
